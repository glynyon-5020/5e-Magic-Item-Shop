# Avrae Alias: `!magic_shop #`

```py
!alias populate_shop embed &1&
<drac2>
num_of_items=max(0,int("&1&")) if "&1&".isdigit() else 1

ci=load_json(get_gvar('d68b763f-bbe5-4ba7-9d5f-3e5cdf089fd0'))['common_items']
ui=load_json(get_gvar('eb672234-7053-4872-9605-4399f65f5621'))['uncommon_items']
ri=load_json(get_gvar('dcf5d0a3-5c21-4226-beea-6617a7a19c6e'))['rare_items']
vi=load_json(get_gvar('d0d98418-d347-4a7f-8c7a-65242b06ade3'))['very_rare_items']
li=load_json(get_gvar('52e00349-8546-4a70-844d-aa95f06b6f91'))['legendary_items']
cr=(1,21)
ur=(21,82)
rr=(82,94)
vr=(94,100)
lr=(100,101)
stock=[]

for _ in range(num_of_items):
	iroll,r,item=randint(100),'',''
	if iroll in range(cr[0],cr[1]):
		item=ci[randint(len(ci)-1)]
		r='Common'
	elif iroll in range(ur[0],ur[1]):
		item=ui[randint(len(ui)-1)]
		r='Uncommon'
	elif iroll in range(rr[0],rr[1]):
		item=ri[randint(len(ri)-1)]
		r='Rare'
	elif iroll in range(vr[0],vr[1]):
		item=vi[randint(len(vi)-1)]
		r='Very Rare'
	elif iroll in range(lr[0],lr[1]):
		item=li[randint(len(li)-1)]
		r='Legendary'
	else:
		pass
	stock.append(f'1d100 ({iroll}) = `{iroll}` - {item} ({r})\n')

T = f"The Magic Item Shop"
D = f"{' '.join(stock)}"
F = f"`!populate_shop #` # = items to generate"
</drac2>
-title "{{T}}"
-desc "{{D}}"
-f "{{F}}"
-color 9c27b0
-thumb https://i.ibb.co/qk5rx2n/shop-removebg-preview.png
```
