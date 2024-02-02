// import React from 'react'

import { useParams } from "react-router-dom";

const NewEntry = () => {
  const params = useParams();
  return (
    <div>
      <h3>NewEntry in {params.cat_id}</h3>
    </div>
  );
};

export default NewEntry;
