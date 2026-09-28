import pytest
from core import rank

def test_text_match():assert rank('blue striped fabric')[0]['name']=='Blue striped fabric'
def test_image_self_similarity():
 rows=rank('',image_id='M01');assert rows[0]['id']=='M01' and rows[0]['visual_score']==1

def test_category_filter():assert all(x['category']=='tile' for x in rank('blue',category='tile'))
@pytest.mark.parametrize('args',[{'weight':2},{'weight':float('nan')},{'image_id':'../secret'},{'category':'bad'},{'query':''}])
def test_invalid(args):
 with pytest.raises(ValueError):rank(**args)
