import React, {Component} from 'react'
import { connect } from 'react-redux'
import PropTypes from 'prop-types'
import { addLead } from '../../actions/leads.js'



export class Form extends Component{
    state = {
        name: '',
        email: '',
        message: ''
    }
    static propTypes = {
        addLead: PropTypes.func.isRequired
    }

    onChange = e => this.setState({[e.target.name]: e.target.value})
    
    onSubmit = e => {
        e.preventDefualt();
        const { name, email, message } = this.state
        const lead = { name, email, message }
        this.props.addLead(lead)
    }

    render() {
        const { name, email, message } = this.state
        return(
            <div>
                <h2>Add Lead</h2>
                <form onSubmit={this.onSubmit}>
                    <div>
                        <label >Name</label>
                        <input type="text" name="name" onChange={this.onChange} value={name} />
                    </div>
                    <div>
                        <label >Email</label>
                        <input type="email" name="email" onChange={this.onChange} value={email} />
                    </div>
                    <div>
                        <label >Message</label>
                        <input type="text" name="message" onChange={this.onChange} value={message} />
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    }
}

export default connect(null, { addLead })(Form)
