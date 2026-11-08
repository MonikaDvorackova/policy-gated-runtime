from dataclasses import dataclass, field
from enum import Enum
import json, sys
class State(str,Enum): PENDING='PENDING'; BLOCKED='BLOCKED'; VALID='VALID'
@dataclass
class Run:
    run_id:str; evaluation:bool=False; risk:bool=False; human:bool=False; state:State=State.PENDING; events:list=field(default_factory=list)
    def record(self,gate:str,approved:bool):
        if gate not in {'evaluation','risk','human'}: raise ValueError('unknown gate')
        setattr(self,gate,approved); self.events.append({'gate':gate,'approved':approved})
        if self.state is State.BLOCKED: return self.state
        if not approved: self.state=State.BLOCKED
        elif self.evaluation and self.risk and self.human: self.state=State.VALID
        else: self.state=State.PENDING
        return self.state
    def may_deploy(self): return self.state is State.VALID
    def export(self): return {'run_id':self.run_id,'state':self.state.value,'gates':{'evaluation':self.evaluation,'risk':self.risk,'human':self.human},'events':self.events}
if __name__=='__main__':
    r=Run('demo-42')
    for gate in ('evaluation','risk','human'): print(gate,r.record(gate,True).value)
    print(json.dumps(r.export(),indent=2)); print('deploy_allowed=',r.may_deploy())
