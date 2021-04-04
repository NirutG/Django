import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Hello World!!
          </p>
          <a
            className="App-link"
            // href="https://reactjs.org"
            href="https://www.youtube.com" // modify to go to Youtube
            target="_blank"
            rel="noopener noreferrer"
          >
            Go to Youtube by NirutG
          </a>
        </header>
      </div>
    );
  }
}

export default App;
