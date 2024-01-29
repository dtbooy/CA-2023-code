import React, { useEffect, useState } from 'react'

const BitcoinIndex = () => {

    // let [currency, setCurrency ] = useState("AUD")
    let [price, setPrice] = useState("")

useEffect(() => {
        fetch("https://api.coindesk.com/v1/bpi/currentprice/AUD")
        .then(res => res.json())
        .then(data => setPrice(data.bpi.AUD.rate))}, []
    )


    return (
        <div>
            <p>Current Price (AUD) ${price}</p>
        </div>
    )
}

export default BitcoinIndex