import React, { useEffect, useState } from 'react'
import CurrencySelector from './CurrencySelector'

const BitcoinIndex = () => {

    // let [currency, setCurrency ] = useState("AUD")
    let [price, setPrice] = useState("")
    const [currency, setCurrency] = useState("AUD")

    

useEffect(() => {
        fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}`)
        .then(res => res.json())
        .then(data => setPrice(data.bpi[currency].rate))
    }, [currency]
)


    return (
        <div>
            <CurrencySelector setCurrency={setCurrency} />
            <p>Current Price ({currency}) ${price}</p>
        </div>
    )
}

export default BitcoinIndex