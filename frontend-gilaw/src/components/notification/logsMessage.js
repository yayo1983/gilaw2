import { get, formatD } from "../common";
import { Toast } from "primereact/toast";
import { Column } from "primereact/column";
import React, { useState, useEffect, useRef } from "react";
import { DataTable } from "primereact/datatable";

const LogsMessage = () => {
  const toast = useRef(null);
  const [logsMessage, setLogsMessage] = useState([]);

  const showToast = (severity, summary, detail) => {
    toast.current.show({
      severity: severity,
      summary: summary,
      detail: detail,
      life: 3000,
    });
  };

  const getLogsMessage = async () => {
    try {
      let response = await get("api/message/logs");
      // response = JSON.stringify(response);
      if (response.data.status === "fail") {
        showToast("error", "Error", "Error in the request of the logs message");
      } else {
        setLogsMessage(response.data.data);
      }
    } catch (error) {
      setLogsMessage([]);
      showToast("error", "Error", "Error in the request");
    }
  };

  useEffect(() => {
    getLogsMessage();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <Toast ref={toast} />
      <div className="row">
        <div className="col-sm-4"></div>
        <div className="col-sm-4">
          <h2>Log history </h2>
        </div>
        <div className="col-sm-4"></div>
      </div>
      <br />
      <div className="row">
        <div className="col-sm-2  "></div>
        <div className="col-sm-8">
          <DataTable value={logsMessage} responsiveLayout="scroll">
            <Column
              field="created_at"
              header="Date"
              body={(notification) =>
                notification.created_at != null
                  ? formatD(notification.created_at)
                  : ""
              }
            ></Column>
            <Column field="full_name_user" header="Name of the user"></Column>
            <Column field="email" header="Email"></Column>
            <Column field="phone" header="Phone"></Column>
            <Column field="category" header="Category"></Column>
            <Column field="message" header="Message"></Column>
          </DataTable>
        </div>
        <div className="col-sm-4"></div>
      </div>
    </>
  );
};

export default LogsMessage;
