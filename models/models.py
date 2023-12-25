from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, text

from src import db


class Scripts(db.Model):
    __tablename__ = 'scripts'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True, index=True,
                                    comment='Autoincrement primary key')
    name: Mapped[str] = mapped_column(String(length=64), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(length=128))
    code: Mapped[text] = mapped_column(Text)
    author: Mapped[str] = mapped_column(String(length=128))
    author_id: Mapped[int] = mapped_column(db.Integer, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=text('NOW()'), comment="Creation time")
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=text('NOW()'), server_onupdate=text('NOW()'),
                           comment="Modification time")

# script1 = Scripts(
#     name="script1_product",
#     description="Select product filtered by date",
#     code=f"Select product.prod_id, product.prod_name, product.prod_price, count(product.prod_id) from product "
#          f"left join orders_list on product.prod_id = orders_list.prod_id "
#          f"left join user_order on user_order.order_id = orders_list.order_id "
#          f"where month(order_date)='2020-12-14' group by product.prod_id;",
#     author="Петя Петров",
#     author_id=164098,
# )
