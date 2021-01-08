import React, { Component } from 'react';
import Select from 'react-select';

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = { chosenOptions: [] };
  }

  handleChange = (e) => {
    if (e !== null) {
      if (e.length !== undefined) {
        let chosenOptions = e.map((e) => {
          return e.value;
        });
        this.setState({
          chosenOptions: chosenOptions,
        });
      } else {
        this.setState({
          chosenOptions: e.value,
        });
      }
    }
  };
  render() {
    return (
      <div className='form'>
        <h1>{this.props.name}</h1>
        <hr />
        <div className='form-content'>
          <Select
            options={this.props.options}
            isMulti={this.props.isMulti}
            className='select'
            placeholder='Wybierz...'
            onChange={this.handleChange}
          />
          <button
            onClick={() => this.props.handleClick(this.state.chosenOptions)}
          >
            Szukaj
          </button>
        </div>
      </div>
    );
  }
}

export default Form;
