import React from 'react';
import ReactDOM from 'react-dom';

import FormComponents from './FormComponents';
import FormComponent from './FormComponent';

import 'whatwg-fetch';
/**
 * Factory for creating form components for questions
 */
class Form extends React.Component {

    constructor(props) {
        super(props);
        this.state = {formComponents: [],
                      questionTypes: []};

        this.newFormComponent = this.newFormComponent.bind(this);
    }

    /* Lifecycle hooks */

    /* Called if component will mount */
    componentWillMount() {
    }

    /* Runs after component output rendered to DOM */
    componentDidMount() {

        fetch("/question_types/")
            .then(function(response) {
                return response.json();
            })
            .then((json) => {
                this.state.questionTypes = json;
                this.setState(this.state);
            }).catch(function(ex) {
                console.log("Could not get question subtypes");
            })
    }

    /* Runs after removed from DOM */
    componentWillUnmount() {

    }

    /* Need a call to this.setState for button pushes */

    newFormComponent() {
        this.state.formComponents.push({message: "im a component"})
        // TODO -- have a form component chooser widget that provides input to add component
        // TODO -- each child in array should have unique "KEY" prop
        ReactDOM.render(<Form />, document.getElementById('mount'))
    }

    render() {
        return (
            <div>
                <h1>FormBuilder</h1>
                <select name="formComponentTypes">
                    // TODO populate via ajax
                    {this.state.questionTypes.map((qt) => {
                         return <option value="{qt}">{qt}</option>
                    })}
                </select>
                <input type="button" value="Click Me" onClick={this.newFormComponent}></input>
                <div id="formComponentContainer" >
                    <FormComponents componentList={this.state.formComponents} />
                </div>
            </div>
        );
    }
}

ReactDOM.render(<Form />, document.getElementById('mount'))
