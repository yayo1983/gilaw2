import { post } from "../common";
import { Toast } from "primereact/toast";
import { Panel } from "primereact/panel";
import { Button } from "primereact/button";
import { Message } from "primereact/message";
import { Dropdown } from "primereact/dropdown";
import React, { useState, useRef } from "react";
import { InputTextarea } from "primereact/inputtextarea";
import { gql, useMutation } from "@apollo/client";

const CREATE_NOTIFICATION = gql`
  mutation CreateNotification($category: String!, $message: String!) {
    createNotification(category: $category, message: $message) {
      id
      category
      message
    }
  }
`;

const SubmissionMessageG = () => {
  const toast = useRef(null);
  const [category, setCategory] = useState(null);
  const [message, setMessage] = useState("");
  const [errorCategory, setErrorCategory] = useState(false);
  const [errorMessage, setErrorMessage] = useState(false);
  const categories = [
    { name: "Sports", code: "Sports" },
    { name: "Finance", code: "Finance" },
    { name: "Movies", code: "Movies" },
  ];

  const [createNotification, { data, loading, error }] =
    useMutation(CREATE_NOTIFICATION);

  const clearForm = (message) => {
    setCategory("");
    setMessage("");
    setErrorMessage(false);
    setErrorCategory(false);
    showToast("success", "Success", message);
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
    if (message === null || message === "") {
      return false;
    }
    return true;
  };

  const sendMessage = async () => {
    try {
      setErrorCategory(false);
      setErrorMessage(false);
      if (validateCategoryInput() && validateMessageInput()) {
        createNotification({
          variables: { category: category.code, message: message },
        });
        if (loading) return showToast("Info", "Info", "Submitting");

        if (error) return showToast("error", "Error", error.message);

        if (!error && !loading) {
          clearForm("The message has been sent successfully");
        }

        /* if (response.status === "fail") {
          showToast("error", "Error", response.message);
        } else {
          clearForm("The message has been sent successfully");
        }
      } else {
        if (!validateCategoryInput()) {
          setErrorCategory(true);
          showToast("error", "Error", "The category input need selected");
        }
        if (!validateMessageInput()) {
          setErrorMessage(true);
          showToast(
            "error",
            "Error",
            "The input text of the message must  can be filled in the form"
          );
        }*/
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
          <h2>Submission message by GraphQL </h2>
        </div>
        <div className="col-sm-4"></div>
      </div>

      <div className="row">
        <div className="col-sm-4"></div>
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
                  value={message}
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

export default SubmissionMessageG;
