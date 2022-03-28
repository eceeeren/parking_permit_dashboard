import { React } from "react";

function ListItem(props) {
  return (
      <li key={props.list.plate}>
        <div style={{ textAlign: "left" }}>
          Plate Number: {props.list.plate}
          <br />
          Owner: {props.list.owner}
          <br />
          Start Date: {props.list.start_date}
          <br />
          End Date: {props.list.end_date}
          <br />
        </div>
      </li>
  );
}

export default ListItem;