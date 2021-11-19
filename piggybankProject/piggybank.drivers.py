from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.blockchain_format.program import Program
from chia.types.condition_opcodes import ConditionOpcode
from chia.util.ints import uint64
from chia.util.hash import std_hash

from clvm.casts import int_to_bytes

from cdv.util.load_clvm import load_clvm

# good driver code should be the only thing between your chia code and the rest of your application


#  we don't want this in any other part of the code 
PIGGYBANK_MOD = load_clvm("piggybank.clsp", "cdv.examples.clsp")

# Create a piggybank
#  this function will return the curried puzzle
def create_piggybank_puzzle(amount, cash_out_puzhash):
    return PIGGYBANK_MOD.curry(amount, cash_out_puzhash)

#  Generate a solution to contribute to a piggybank
def solution_for_piggybank(pb_coin, contribution_amount):
    return Program.to([pb_coin.amount, (pb_coin.amount + contribution_amount), pg_coin.puzzle_hash])

# return the condition to assert the announcement
def piggybank_announcement_assertion(pb_coin, contribution_amount):
    #  the assertion is the hash of the coin id and the message we are announcing which in this case is new_amount
    return [ConditionOpcode.ASSERT_COIN_ANNOUNCEMENT, std_hash(pb_coin.name() + int_to_bytes(pb_coin.amount + contribution_amount)]