import { React } from "react";
import { format } from "date-fns";

function ListItem(props) {
  return (
      <li key={props.list.plate}>
        <div style={{ textAlign: "left", fontSize: 16 }}>
          Plate Number: {props.list.plate}
          <br />
          Owner: {props.list.owner}
          <br />
          Start Date: {format(new Date(props.list.start_date), "yyyy/MM/dd")}
          <br />
          End Date: {format(new Date(props.list.end_date), "yyyy/MM/dd")}
          <br />
        </div>
      </li>
  );
}

export default ListItem;