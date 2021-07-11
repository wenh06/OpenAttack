========================
AttackEvals API
========================

AttackEval
----------------

.. autoclass:: OpenAttack.AttackEval
    :members: __init__, eval, eval_results

------------------------------------

ChineseAttackEval
-------------------

.. autoclass:: OpenAttack.attack_evals.ChineseAttackEval(OpenAttack.AttackEval)
    :members: __init__, measure, update, get_result, clear, eval, eval_results

DefaultAttackEval
-------------------

.. autoclass:: OpenAttack.attack_evals.DefaultAttackEval(OpenAttack.AttackEval)
    :members: __init__, measure, update, get_result, clear, eval, eval_results

DetailedAttackEval
--------------------

.. autoclass:: OpenAttack.attack_evals.DetailedAttackEval(OpenAttack.AttackEval)
    :members: __init__, measure, update, get_result, clear, eval, eval_results

InvokeLimitedAttackEval
-------------------------

.. autoclass:: OpenAttack.attack_evals.InvokeLimitedAttackEval(OpenAttack.AttackEval)
    :members: __init__, measure, update, get_result, clear, eval, eval_results

