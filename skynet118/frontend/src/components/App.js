import React, {Component, Fragment} from 'react'
import ReactDOM from 'react-dom'

import Header from './layout/Header'
import Dashboard from './leads/Dashboard'

import { Provider } from 'react-redux'
import store from '../store'


class App extends Component{
    render() {
        return(
            <Provider store={store}>
                <Fragment>
                    <Header />
                    <h1> Testing ReactJS with Django</h1>
                    <Dashboard />
                </Fragment>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))


