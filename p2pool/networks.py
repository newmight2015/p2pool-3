from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    gamecoin=math.Object(
        PARENT=networks.nets['gamecoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c6923610'.decode('hex'),
        PREFIX='7208c1a53ef659b0'.decode('hex'),
        P2P_PORT=12067,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=1436,
        BOOTSTRAP_ADDRS='trmserver.no-ip.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
    gamecoin_testnet=math.Object(
        PARENT=networks.nets['gamecoin_testnet'],
        SHARE_PERIOD=4, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c7923110'.decode('hex'),
        PREFIX='7208c1a54ef619b0'.decode('hex'),
        P2P_PORT=18777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
