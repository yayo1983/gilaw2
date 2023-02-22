import { formatD } from "../common";
import { Toast } from "primereact/toast";
import { Column } from "primereact/column";
import React, { useRef } from "react";
import { DataTable } from "primereact/datatable";
import { gql, useQuery } from "@apollo/client";

const GET_DATA = gql`
  query GetLogNotifications {
    allLogs {
      fullNameUser
      email
      phone
      category
      createdAt
      message
    }
  }
`;

const LogsMessageG = () => {
  const toast = useRef(null);
  const { loading, error, data } = useQuery(GET_DATA);

  const showToast = (severity, summary, detail) => {
    toast.current.show({
      severity: severity,
      summary: summary,
      detail: detail,
      life: 3000,
    });
  };

  return (
    <>
      <Toast ref={toast} />
      <div className="row">
        <div className="col-sm-4"></div>
        <div className="col-sm-4">
          <h2>Log history by GraphQL </h2>
        </div>
        <div className="col-sm-4"></div>
      </div>
      <br />
      <div className="row">
        <div className="col-sm-2"></div>
        <div className="col-sm-8">
        {data && data.allLogs && <DataTable value={data.allLogs} responsiveLayout="scroll">
            <Column
              field="createdAt"
              header="Date"
              body={(notification) =>
                notification.createdAt != null
                  ? formatD(notification.createdAt)
                  : ""
              }
            ></Column>
            <Column field="fullNameUser" header="Name of the user"></Column>
            <Column field="email" header="Email"></Column>
            <Column field="phone" header="Phone"></Column>
            <Column field="category" header="Category"></Column>
            <Column field="message" header="Message"></Column>
          </DataTable>} 
        </div>
        <div className="col-sm-4"></div>
      </div>
    </>
  );
};

export default LogsMessageG;
