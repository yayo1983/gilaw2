import React from "react";
import { Link } from "react-router-dom";

const NavBar = () => {
  return (
    <div className="row">
      <div className="col-sm-4"></div>
      <div className="col-sm-4">
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
          <div className="container-fluid">
            <div
              className="collapse navbar-collapse"
              id="navbarSupportedContent">
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <Link className="nav-link active" aria-current="page" to="/">
                    Home
                  </Link>
                </li>
                <li className="nav-item">
                  {/* <Link className="nav-link" to="/login">
                    Login
                  </Link> */}
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/message/submission">
                    Submission message API REST
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/message/submissionG">
                    Submission message with GraphQL
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/message/logs">
                    Log history API REST
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/message/logs2">
                    Log history with GraphQL
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
      <div className="col-sm-4"></div>
    </div>
  );
};

export default NavBar;
