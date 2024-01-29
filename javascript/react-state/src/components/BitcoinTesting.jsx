import React, { useEffect, useState } from 'react'

const BitcoinIndex = () => {

    let [currency, setCurrency] = useState("AUD")
    let [price, setPrice] = useState(currency)

    useEffect(() => {
        fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}`)
            .then(res => res.json())
            .then(res => {console.log(currency, res); return res})
            .then(data => setPrice(data.bpi[currency].rate))
    }, [currency]
    )

    const currencySelectHandler = (event) => {
        setCurrency(event.target.value)
    }


    return (
        <div>
            <p>Current Price ({currency}) ${price}</p>
            <label >Choose Currency:</label>
            <select id="currency" name="currency">
                <option value="AUD" onSelect={currencySelectHandler}>AUD</option>
                <option value="USD" onSelect={currencySelectHandler}>USD</option>
                <option value="EUR" onSelect={currencySelectHandler}>EUR</option>
            </select>
        </div>
    )
}

export default BitcoinIndex