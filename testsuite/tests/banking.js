const chai = require("chai");
const server = "http://127.0.0.1:8000/api"
const chaiHttp = require("chai-http");


//assertions
chai.should();
chai.use(chaiHttp);


describe('BANK ACCOUNTS API', () => {

	//get all Bank Accounts
	describe("GET /banking/bank-accounts/", () => {
		it("It should Get all Bank Accounts", (done) => {
			chai.request(server)
				.get("/banking/bank-accounts")
				.end((err, response) => {
					response.should.have.status(200);
					response.body.should.be.a('array');
					//response.body.length.should.be.eq(6)
				done();
				})
		})
/*
		it("It should not GET Bank Accounts", (done) => {
			chai.request(server)
				.get("/bank")
				.end((err, response) => {
					response.should.have.status(404);
				done();
				})
		})
		*/
	})

})