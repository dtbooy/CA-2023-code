// import React from 'react'

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const NewEntry = ({ categories, addEntry }) => {
  const params = useParams();
  const [entry, setEntry] = useState("")
  // const [newEntry, setNewEntry] = useState({})

  // useEffect(() => {

  // },[]);

  const handleChange = (e) => {
    setEntry(e.target.value)
  }
  const handleSubmit = (event) => {
    event.preventDefault()

    addEntry(params.cat_id, entry)
  // 3. clear form
  setEntry("")
  // 4. redirect to where the display is

  }

  return (
    <div className="container">
      <h3>NewEntry in {categories[params.cat_id]}</h3>
      <form className="section" onSubmit={handleSubmit}>
        <div className="field">
          <label className="label">Entry</label>
          <div className="control">
            <textarea onChange={handleChange} value={entry} className="textarea" placeholder="Textarea"></textarea>
          </div>
        </div>
        <div className="control">
          <button className="button is-link">Create Entry</button>
        </div>
      </form>
    </div>
  );
};

export default NewEntry;
