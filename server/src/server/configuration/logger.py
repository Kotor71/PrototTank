import logging
import sys

errfmt = logging.Formatter('%(asctime)-15s %(boxip)s - %(levelname)s - Code %(errcode)d found in %(source)s : %(message)s')
dbgfmt = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")


hdbg = logging.StreamHandler(sys.stdout)
hdbg.setLevel(logging.DEBUG)
hdbg.setFormatter(dbgfmt)

logger = logging.getLogger('ProtoTank')
logger.setLevel(logging.DEBUG)
logger.addHandler(hdbg)


class ProtoTankException(Exception):
    def __init__(self, message):
        self.message=message

