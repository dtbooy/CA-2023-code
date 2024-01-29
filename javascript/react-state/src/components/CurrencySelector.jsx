import React, { useState } from 'react'

const CurrencySelector = ({setCurrency}) => {
    const [currencySelect, setCurrencySelect] = useState("AUD")

    useEffect(() => {setCurrency = (currencySelect),[currencySelect]})
    
    return (
        <select value={currencySelect} onChange={(event)=>setCurrencySelect(event.target.value)}>
            <option value="AUD"> AUD </option>
            <option value="USD"> USD </option>
            <option value="EUR"> EUR </option>
        </select>
    )
}

export default CurrencySelector