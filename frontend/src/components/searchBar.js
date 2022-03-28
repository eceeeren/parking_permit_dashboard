import { React } from "react";

function SearchBar(props) {
  return (
    <div className="search">
      <input placeholder={props.placeholder} onChange={props.onChange} />
    </div>
  );
}

export default SearchBar;
