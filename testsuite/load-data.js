const accounts = require("./data");
const axios = require("axios");
const schedule = require("node-schedule");
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ4MjcwNDIzLCJpYXQiOjE2NDU2Nzg0MjMsImp0aSI6IjAzNDFjOTcyZGZkMDQ5YTU4Y2IwNTk5ZGQyYjkxNTQyIiwidXNlcl9pZCI6MX0.VeWDUngFzkDwv9MfSpFpH7DmLqDD8xyWcnmEvMMxE_o"

const headers = { Authorization: `Bearer ${token}` };


accounts.forEach(account => {
    console.log(account.account_number)
    let url = 'http://127.0.0.1:8000/api/banking/bank-accounts/'
    axios.post(url, 
    {
        "account_number": account.account_number,
        "bank_name": account.bank_name,
        "account_name": account.account_name,
        "account_type": account.account_type,
        "balance": account.balance,
        "user": account.user
    },
    { headers }
    )
    .then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.log(error)
    })
});
