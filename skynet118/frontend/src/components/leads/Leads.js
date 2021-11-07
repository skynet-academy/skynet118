import React, {Component, Fragment } from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { getLeads, deleteLead } from '../../actions/leads'

export class Leads extends Component {
    static PropTypes = {
        leads: PropTypes.array.isRequired,
        getLeads: PropTypes.func.isRequired,
        deleteLead: PropTypes.func.isRequired
    }
    
    componentDidMount(){
        this.props.getLeads()
    }

    render(){
        return(
           <Fragment>
               <h2>Leads</h2>
               <table>
                   <thead>
                       <tr>
                           <td>ID</td>
                           <td>Name</td>
                           <td>Email</td>
                           <td>Message</td>
                       </tr>
                   </thead>
                   <tbody>
                       { this.props.leads.map( lead => (
                           <tr key={ lead.id }>
                               <td>{ lead.id }</td>
                               <td>{ lead.name }</td>
                               <td>{ lead.email }</td>
                               <td>{ lead.message }</td>
                               <td><buttom 
                                    onClick={this.props.deleteLead.bind(this, lead.id)}
                                    className="button-danger">{" "} Delete</buttom></td>
                           </tr>
                       ))}
                   </tbody>
               </table>
               <h1>Leads list</h1>
           </Fragment>
        )
    }
}

const mapStateTopProps = state => ({
     leads: state.leads.leads
})

export default connect(mapStateTopProps, { getLeads, deleteLead })(Leads)
