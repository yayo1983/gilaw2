import NavBar from "./components/NavBar";
import Login from "./components/user/login";
import Initial from "./components/notification/initial";
import LogsMessage from "./components/notification/logsMessage";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SubmissionMessage from "./components/notification/submissionMessage";
import LogsMessageG from "./components/notification/logsMessageG";

function App() {
  return (
      <BrowserRouter>
        <NavBar />
        <div className="container-fluid my-4">
          <Routes>
            <Route exact path="/" element={<Initial />} />
            <Route exact path="/login" element={<Login />} />
            <Route
              exact
              path="/message/submission"
              element={<SubmissionMessage />}
            />
            <Route exact path="/message/logs" element={<LogsMessage />} />
            <Route exact path="/message/logs2" element={<LogsMessageG />} />
          </Routes>
        </div>
      </BrowserRouter>
  );
}

export default App;
