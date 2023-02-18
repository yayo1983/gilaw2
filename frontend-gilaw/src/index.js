import React from 'react';
import ReactDOM from 'react-dom/client';
import NavBar from './components/NavBar';
import Login from './components/user/login';
import Initial from './components/notification/initial';
import LogsMessage from './components/notification/logsMessage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SubmissionMessage from './components/notification/submissionMessage';
import reportWebVitals from './reportWebVitals';
import "bootstrap/dist/css/bootstrap.min.css"
import './index.css';
//theme
import "primereact/resources/themes/lara-light-indigo/theme.css";     
//core
import "primereact/resources/primereact.min.css";
//icons
import "primeicons/primeicons.css";  

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
          <NavBar />
          <div className='container-fluid my-4'>
            <Routes>
              <Route exact path='/' element={<Initial />}/> 
              <Route exact path='/login' element={<Login />}/> 
              <Route exact path='/message/submission' element={<SubmissionMessage />}/> 
              <Route exact path='/message/logs' element={<LogsMessage />}/>
            </Routes>
          </div>
    </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
