from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    try:
        rule = env.ref('connector_ecommerce.excep_product_has_checkpoint')
    except ValueError:
        rule = None
    if rule:
        rule.unlink()
