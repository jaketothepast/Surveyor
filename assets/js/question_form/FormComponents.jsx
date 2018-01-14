import React from 'react'

import FormComponent from './FormComponent'

export default class FormComponents extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (this.props.componentList.map((component) => (
                <FormComponent message={component.message} />))
        )
    }
}
