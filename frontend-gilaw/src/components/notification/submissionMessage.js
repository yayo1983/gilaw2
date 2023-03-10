import { post } from "../common";
import { Toast } from "primereact/toast";
import { Panel } from "primereact/panel";
import { Button } from "primereact/button";
import { Message } from "primereact/message";
import { Dropdown } from "primereact/dropdown";
import React, { useRef } from "react";
import { InputTextarea } from "primereact/inputtextarea";
import { useSelector, useDispatch } from "react-redux";
import { notificationActions } from '../../store/notification';

const SubmissionMessage = () => {
  const dispatch = useDispatch();
  const category = useSelector((state) =>state.notificationr.category);
  const messageNotification = useSelector((state) =>state.notificationr.messageNotification);
  const errorCategory = useSelector((state) =>state.notificationr.errorCategory);
  const errorMessage = useSelector((state) =>state.notificationr.errorMessage);
  const toast = useRef(null);
  const categories = [
    { name: "Sports", code: "Sports" },
    { name: "Finance", code: "Finance" },
    { name: "Movies", code: "Movies" },
  ];

  const setCategory = (value) =>{
    dispatch(notificationActions.setCategory(value));
  };

  const setMessage = (value) =>{
    dispatch(notificationActions.setMessage(value));
  };

    const showToast = (severity, summary, detail) => {
    toast.current.show({
      severity: severity,
      summary: summary,
      detail: detail,
      life: 3000,
    });
  };

  const validateCategoryInput = () => {
    if (category === null || category === "") {
      return false;
    }
    return true;
  };

  const validateMessageInput = () => {
    if (messageNotification === null || messageNotification === "") {
      return false;
    }
    return true;
  };

  const sendMessage = async () => {
    console.log(category, messageNotification)
    try {
      dispatch(notificationActions.setErrorCategory(false));
      dispatch(notificationActions.setErrorMessage(false));
      if (validateCategoryInput() && validateMessageInput()) {
        let data = {
          category: category.code,
          message: messageNotification,
        };
        let response = await post("api/message/submission", data);
        response = JSON.stringify(response);
        if (response.status === 'fail') {
          showToast("error", "Error", response.message);
        } else {
          dispatch(notificationActions.clearForm());
          showToast("success", "Success", "The message has been sent successfully");
        }
      } else {
        if (!validateCategoryInput()) {
          dispatch(notificationActions.setErrorCategory(true));
          showToast("error", "Error", "The category input need selected");
        }
        if (!validateMessageInput()) {
          dispatch(notificationActions.setErrorMessage(true));
          showToast(
            "error",
            "Error",
            "The input text of the message must  can be filled in the form"
          );
        }
      }
    } catch (error) {
      console.log(error);
      showToast("error", "Error", "Error sending the message");
    }
  };

  let classErrorCategory = errorCategory ? "p-invalid mr-2" : "";
  let classErrorMessage = errorMessage ? "p-invalid mr-2" : "";

  return (
    <>
      <Toast ref={toast} />
      <div className="row">
        <div className="col-sm-4"></div>
        <div className="col-sm-4">
          <h2>Submission message </h2>
        </div>
        <div className="col-sm-4"></div>
      </div>

      <div className="row">
        <div className="col-sm-2"></div>
        <div className="col-sm-8">
          <Panel header="Submission form">
            <div className="mb-3">
              Category:
              <br />
              <span className="p-input-icon-left">
                <Dropdown
                  filter
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  options={categories}
                  optionLabel="name"
                  placeholder="Select a category"
                  className={classErrorCategory}
                  tooltip="Category of the message"
                />
              </span>
              {errorCategory && (
                <Message severity="error" text="Error in the category" />
              )}
            </div>
            <div className="mb-3">
              Message:
              <br />
              <span className="p-input-icon-left">
                <InputTextarea
                  rows={5}
                  cols={30}
                  required
                  value={messageNotification}
                  placeholder="Message"
                  tooltip="Put the message"
                  className={classErrorMessage}
                  onChange={(e) => setMessage(e.target.value)}
                />
              </span>
              {errorMessage && (
                <Message severity="error" text="Error in the message" />
              )}
            </div>
            <div className="flex flex-wrap align-items-center justify-content-left">
              <Button label="Send" icon="pi pi-check" onClick={sendMessage} />
            </div>
          </Panel>
          <div className="col-sm-4"></div>
        </div>
      </div>
    </>
  );
};

export default SubmissionMessage;
