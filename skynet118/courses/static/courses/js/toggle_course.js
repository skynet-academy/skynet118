$(document).on('change', '#course_selection', function(e){
    e.preventDefault();
    console.log("working");
    $.ajax({
        type:'POST',
        url: '/courses',
        data: {
            name: $("#course.course_name").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data){
            $('#intro').html(data) 
        }
    });
});
