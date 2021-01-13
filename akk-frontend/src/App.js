import './App.css';
import React, { Component } from 'react';
import Header from './components/Header';
import Form from './components/Form';
import 'react-accessible-accordion/dist/fancy-example.css';
import {
  Accordion,
  AccordionItem,
  AccordionItemButton,
  AccordionItemHeading,
  AccordionItemPanel,
} from 'react-accessible-accordion';

const axios = require('axios');

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [],
      recipes: [],
      recommend: [],
      recommendList: [],
      onStart: true,
    };
  }

  componentDidMount = () => {
    axios
      .get('http://localhost:5000/products')
      .then((response) => {
        let options = response.data.map((el) => {
          return { value: el, label: el };
        });
        this.setState({ products: options });
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
    axios
      .get('http://localhost:5000/recipes')
      .then((response) => {
        // handle success
        let recipes = response.data.map((el) => {
          return { value: el, label: el };
        });
        this.setState({ recipes: recipes });
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
  };

  findOneRecepie = (skladnik) => {
    this.setState({
      recommendList: [],
      onStart: false,
    });
    axios
      .post('http://localhost:5000/showrecipe', {
        skladnik,
      })
      .then((response) => {
        let recipe_object = response.data[Object.keys(response.data)];

        this.setState({
          recommend: {
            name: recipe_object.Nazwa_Przepisy,
            description: recipe_object.Przepis,
            products: recipe_object.Składniki,
          },
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  findRecepies = (skladniki) => {
    this.setState({
      recommend: [],
      onStart: false,
    });
    axios
      .post('http://localhost:5000/recommend', {
        skladniki,
      })
      .then((response) => {
        let keys = Object.keys(response.data);
        let recipes = [];
        for (const el of keys) {
          recipes.push({
            name: response.data[el].Nazwa_Przepisy,
            description: response.data[el].Przepis,
            products: response.data[el].Składniki,
            probability: response.data[el].prawdopodobienstwo,
          });
        }
        this.setState({
          recommendList: recipes,
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  render() {
    return (
      <div className='app'>
        <Header />
        <div className='content'>
          <div className='forms'>
            <Form
              name='Szukaj wg nazwy przepisu'
              options={this.state.recipes}
              isMulti={false}
              handleClick={this.findOneRecepie}
            />
            <Form
              name='Szukaj wg produktów'
              options={this.state.products}
              isMulti={true}
              handleClick={this.findRecepies}
            />
          </div>
          <div className='results'>
            {this.state.onStart ? (
              <h1>
                Skorzystaj z jednej z wyszukiwarek aby wyświetlić przepisy
              </h1>
            ) : (
              ''
            )}
            {this.state.recommend.length === 0 ? (
              ''
            ) : (
              <div>
                <h1>{this.state.recommend.name}</h1>
                <div className='recipe-content'>
                  <div className='description'>
                    <p>{this.state.recommend.description}</p>
                  </div>
                  <div className='products'>
                    <p>Składniki:</p>
                    {this.state.recommend.products !== undefined
                      ? this.state.recommend.products.map((el) => {
                          return (
                            <li>
                              {el.Nazwa_Składniki} - {el.Ilość}{' '}
                              {el.Typ !== 'nieokreślone' ? el.Typ : ''}
                            </li>
                          );
                        })
                      : ''}
                  </div>
                </div>
              </div>
            )}
            {this.state.recommendList.length === 0 ? (
              ''
            ) : (
              <div>
                <Accordion>
                  {this.state.recommendList.map((el, index) => {
                    {
                      return (
                        <AccordionItem key={index}>
                          <AccordionItemHeading>
                            <AccordionItemButton>
                              {el.name} ({el.probability}%)
                            </AccordionItemButton>
                          </AccordionItemHeading>
                          <AccordionItemPanel>
                            <div className='description'>{el.description}</div>
                            <div className='products'>
                              <p>Składniki:</p>
                              {el.products.map((p) => {
                                return (
                                  <li key={p.Nazwa_Składniki}>
                                    {p.Nazwa_Składniki} - {p.Ilość}{' '}
                                    {p.Typ !== 'nieokreślone' ? p.Typ : ''}
                                  </li>
                                );
                              })}
                            </div>
                          </AccordionItemPanel>
                        </AccordionItem>
                      );
                    }
                  })}
                </Accordion>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
