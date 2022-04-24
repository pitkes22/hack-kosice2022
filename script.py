import pandas as pd
from sklearn.svm import SVC
# purchased_producs=pd.read_csv('./purchased_producs.csv', sep=',')
# catalog_items=pd.read_csv('./catalog_items.csv', sep=',')
# visited_products=pd.read_csv('./visited_products.csv', sep=',', nrows=200)
#
# # using merge function by setting how='inner'
# merged_data = pd.merge(purchased_producs, catalog_items,
#                        on='product_id',
#                        how='inner')
#
#
# vvvv_merged_data = pd.merge(merged_data, visited_products,
#                        on='product_id',
#                        how='inner')
# print(vvvv_merged_data)

target_group=pd.read_csv('./target_group.csv', sep=',')
purchased_producs=pd.read_csv('./purchased_producs.csv', sep=',')

test_data = pd.merge(target_group, purchased_producs,
                       on='customer_id',
                       how='inner')

visited_products=pd.read_csv('./visited_products.csv', sep=',').groupby(['customer_id', 'product_id']).size().reset_index(name="count").sort_values(by=['customer_id', 'count']).drop_duplicates(subset=['customer_id'], keep='last').reset_index(drop=True)
catalog_items=pd.read_csv('./catalog_items.csv', sep=',')
visited_products_extended = pd.merge(catalog_items, visited_products,
                       on='product_id',
                       how='inner')

viewed_items = pd.merge(target_group, visited_products_extended,
                       on='customer_id',
                       how='inner')

train_data = pd.merge(target_group, purchased_producs,
                       on='customer_id',
                       how='inner')

clf = SVC()
clf.fit()


# sorted = viewed_items.sort_values(by=['customer_id', 'timestamp'])
# uniw = sorted.drop_duplicates(subset=['customer_id'], keep='last').reset_index(drop=True)
# uniw = sorted.groupby('customer_id').head(5).reset_index(drop=True)

# print(uniw)

# uniw.to_csv('out.csv', header=['customer_id', 'product_id'], columns=['customer_id', 'product_id'], index=False)

breakpoint()

# for index, row in target_group.iterrows():
#     print(index)
#     target = row['customer_id']
#     v = visited_products.where(visited_products['customer_id']==target)
#     print(v)
# print(target_group)

