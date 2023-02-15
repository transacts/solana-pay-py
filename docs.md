Methods:

**build_transaction** 


    Parameters:
    | publickey - The public key of the account reciving the payment |
    | amount - the amount of SOL to be requested |
    | fill color - the color of the QR code design (in hex) | *optional* 
    | background color - the background color of the QR code (in hex) | *optional*

RETURNS A LIST: 
    ```[invoice_id, publickey, base64_image]```

Example: ```build_transaction('3WbQVasKH9sqrp3NT5ZWVQMBupiuwcBDXzkMypM2koq6', 1, "#593933", "939393")```

**get_payment_status**

    Parameters:
    | invoice_id - the invoice ID that was returned when you built the transaction | 
    | publickey - the publickey you used to build the transaction | 
    
Returns either ```True ```if paid or ```False``` if not paid
