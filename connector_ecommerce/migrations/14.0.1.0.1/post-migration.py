from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    rule = env.ref(
        "connector_ecommerce.excep_product_has_checkpoint",
        raise_if_not_found=False,
    )
    if rule:
        rule.unlink()
