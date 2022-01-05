from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Order, Course, Package, Purchase
import json, os, sys 
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

#from paypalcheckoutsdk

from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest

# Create your views here.

def simple_checkout(request):
    return render(request, 'payments/simple_checkout.html')

def checkout(request, pk, name):
    customer = request.user 
    course = Course.objects.get(id=pk)
    package = Package.objects.filter(course_package=pk, package_name=name)[0]
    #package = Package.objects.filter(course_package=pk).filter(package_name=name).only()
    if(request.method == "POST"):
        package = Package.objects.filter(course_package=pk, package_name=name)[0]
        data = json.loads(request.body)
        order_id = data['orderID']
        details = GetOrder().get_order(order_id)
        detail_price = float(details.result.purchase_units[0].amount.value)
        if(detail_price == float(package.price)):
            trans = CaptureOrder().capture_order(order_id, debug=True)
            purchase = Purchase(
                    purchase_id = trans.result.id,
                    state = trans.result.status,
                    cod_state = trans.status_code,
                    product = package.package_name,
                    total = trans.result.purchase_units[0].payments.captures[0].amount.value,
                    name = trans.result.payer.name.given_name,
                    surname = trans.result.payer.name.surname,
                    email = trans.result.payer.email_address,
                    address = trans.result.purchase_units[0].shipping.address.address_line_1,
                    )
            purchase.save()
            data = {
                "id": f"{trans.result.id}",
                "name": f"{trans.result.payer.name.given_name}",
                "message": "Purchase done successfully"
            }
            return JsonResponse(data)
        else:
            data = {
                "name": "error",
                "message": "We could not finish your purchase"
                    }
            return JsonResponse(data)


    context = {'package': package, 'course': course, 'customer': customer}
    return render(request, 'payments/checkout.html', context)

def cart(request):
    if(request.user.is_authenticated):
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items  = []
    context = {'items': items}
    return render(request, 'payments/cart.html', context)

def payment_complete(request):
    body = json.loads(request.body)
    context = {
        "body": body
            }
    #course = Course.objects.get(id=body['course_id'])
    #Order.objects.create(course=course)
    return HttpResponseRedirect("/")

class PayPalClient:

    def __init__(self):
        #self.client_id =  os.environ["PAYPAL-CLIENT-ID"] if 'PAYPAL-CLIENT-ID' in os.environ else "AWw0wNEoQtKQsAlFgFUjx59Qs7CZSCujq01Ml-cysbffLlvHpFHPcqg1lKNRO5SffFKszQeZVqQ56G77"
        self.client_id =  os.environ["PAYPAL-CLIENT-ID"] if 'PAYPAL-CLIENT-ID' in os.environ else "AZtrmMXHZ-sTMmTsk3eIzoItkqZTXFXvUo74qInK8MZbOcCsZDlJ0as3qRRSDHVIpbrEJtywf_JH-Dda"
        #self.client_secret = os.environ["PAYPAL-CLIENT-SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else "EMfOdmE60zetRvaOR5GesXeFnLgMQ5SzVo4A-FSRDOCmzMZ0DWlrOSRsqs601W3sp0hW-1xIAkA6KxBR"
        self.client_secret = os.environ["PAYPAL-CLIENT-SECRET"] if 'PAYPAL_CLIENT_SECRET' in os.environ else "EOzueLV13bWEyg-zt9D1o3eJKAGK9iY4n-MB8xUkUVJkSL4XKYPdtFasyM_5jh_anQnbx5C5-XKvAXzA"

        """Set up and return PayPal Python SDK environment with PayPal Access credentials.
           This sample uses SandboxEnvironment. In production, use
           LiveEnvironment."""

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        """ Returns PayPal HTTP client instance in an environment with access credentials. Use this instance to invoke PayPal APIs, provided the

            credentials have access. """
        self.client = PayPalHttpClient(self.environment)
    def object_to_json(self, json_data):
        """
	        Function to print all json data in an organized readable manner
	    """
        result = {}
        if(sys.version_info[0] < 3):
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()

        for key,value in itr:	
	        # Skip internal attributes.
            if(key.startswith("__")):
	            continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else self.object_to_json(value) if not self.is_primittive(value) else value
	
        return result;
	
    def array_to_json_array(self, json_array):
        result =[]
        if(isinstance(json_array, list)):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
	
        return result;
	
    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


class GetOrder(PayPalClient):
  """You can use this function to retrieve an order by passing order ID as an argument"""   

  def get_order(self, order_id):
    """Method to get order"""
    request = OrdersGetRequest(order_id)

    #3. Call PayPal to get the transaction
    response = self.client.execute(request)
    return response
    #4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
    #print('Status Code: ', response.status_code)
    #print('Status: ', response.result.status)
    #print('Order ID: ', response.result.id)
    #print('Intent: ', response.result.intent)
    #print('Links:')

    #for link in response.result.links:
    #    print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
    #    print('Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code, response.result.purchase_units[0].amount.value))


class CaptureOrder(PayPalClient):
  #2. Set up your server to receive a call from the client
  """this sample function performs payment capture on the order.
  Approved order ID should be passed as an argument to this function"""

  def capture_order(self, order_id, debug=False):
    """Method to capture order using order_id"""
    request = OrdersCaptureRequest(order_id)
    #3. Call PayPal to capture an order
    response = self.client.execute(request)
    #4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
    if(debug):
      print('Status Code: ', response.status_code)
      print('Status: ', response.result.status)
      print('Order ID: ', response.result.id)
      print('Links: ')
      for link in response.result.links:
          print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
          print('Capture Ids: ')

      for purchase_unit in response.result.purchase_units:
          for capture in purchase_unit.payments.captures:
              print('\t', capture.id)
      #print("Buyer:")
      #print("\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
      #  response.result.payer.name.given_name + " " + response.result.payer.name.surname,
      #  response.result.payer.phone.phone_number.national_number))
    return response

