import React, {useState, useEffect, Component} from 'react';
import './App.css';
import 'semantic-ui-css/semantic.min.css';


 function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(()=>{
    fetch('/api').then(
      response => response.json()
    ).then(data => setInitialData(data))
  }, []);
  const { tags, suggestions } = this.state;
  return (
    <div className="App">
      <table class="ui celled table">
  <thead>
    <tr><th>UserId</th>
    <th>Title</th>
    <th>Completed</th>
  </tr></thead>
  <tbody>
    <tr>
      <td data-label="userId">{initialData.userId}</td>
      <td data-label="title">{initialData.title}</td>
      <td data-label="completed">{initialData.completed}</td>
    </tr>
  </tbody>
 </table>
    </div>
  );
}


export default App;