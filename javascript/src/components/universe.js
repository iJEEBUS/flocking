/******************************************************************
 * The universe that will display the boids as they fly.
 * 
 * @author Ron Rounsifer
 ******************************************************************/
import React, { Component } from 'react';
import P5Wrapper from 'react-p5-wrapper';
import sketch from './sketch';
import '../styling/universe.css';

import { 
    Layout,
    Menu, 
    Icon, 
    Button
  } from 'antd';
import '../styling/universe.css';

const { Sider, Header, Footer, Content } = Layout;

/******************************************************************
 * A Total Daily Exercise Expenditure calculator form.
 ******************************************************************/
class Universe extends Component {
    state = {
        activate: false,
        collapsed: false,
    };

    toggleCollapsed = () => {
      this.setState({
        collapsed: !this.state.collapsed,
      });
    };

    toggleActivate = () => {
      this.setState({
        activate: !this.state.activate,
      })
    }
  /****************************************************************
   * Render method to display the application.
   ****************************************************************/
  render() {
    return (
      <Layout className="App">
        

        <Layout>
          <Header className="App-header">
            <h1 onClick={this.toggleActivate}>Flocking Algorithm</h1>
          </Header>
          <Content className="App-content" onClick={this.onClick}>     
              { this.state.activate ? <P5Wrapper sketch={sketch} height={300} width={300} /> : null}
          </Content>
        </Layout>
        <Footer className="App-footer">
          &copy; Ron Rounsifer
        </Footer>
        
      </Layout>
      );
  }
}

export default Universe;

// { !this.state.activate ? <h1>Flocking Algorithm</h1> : null }
//             { !this.state.activate ? <h3>Click to begin</h3> : null }