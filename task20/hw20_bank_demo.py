from hw20_bank import Bank


client_id = "0000001"
bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
bank.open_deposit_account(client_id=client_id, start_balance=1000, years=1)
bank.calc_deposit_interest_rate(client_id=client_id)
bank.close_deposit(client_id=client_id)
