### 灰鹱 商店后端
简介： 
#### 开发环境
Python3.6;  
Django2.2.3;  
Mysql5.7  


# 灰鹱商店API 文档
灰鹱商店Api

## Version: v1

**License:** BSD License

### Security
**JWT Token**  

|apiKey|*API Key*|
|---|---|
|Description|jwt令牌认证方式|
|In|header|
|Name|Authorization + Bearer [access]|

### /base/refresh/

#### POST
##### Description:

Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TokenRefresh](#tokenrefresh) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenRefresh](#tokenrefresh) |

### /base/token/

#### POST
##### Description:

Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [TokenObtainPair](#tokenobtainpair) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [TokenObtainPair](#tokenobtainpair) |

### /base/v1/group/

#### GET
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Group](#group) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Group](#group) |

### /base/v1/group/{id}/

#### GET
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 组. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Group](#group) |

#### PUT
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 组. | Yes | integer |
| data | body |  | Yes | [Group](#group) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Group](#group) |

#### PATCH
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 组. | Yes | integer |
| data | body |  | Yes | [Group](#group) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Group](#group) |

#### DELETE
##### Description:

API endpoint that allows groups to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 组. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /base/v1/permission/

#### GET
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | No | string |
| content_type | query |  | No | string |
| codename | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Permission](#permission) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Permission](#permission) |

### /base/v1/permission/{id}/

#### GET
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 权限. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Permission](#permission) |

#### PUT
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 权限. | Yes | integer |
| data | body |  | Yes | [Permission](#permission) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Permission](#permission) |

#### PATCH
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 权限. | Yes | integer |
| data | body |  | Yes | [Permission](#permission) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Permission](#permission) |

#### DELETE
##### Description:

API endpoint that allows permission to be viewed or edited.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this 权限. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /base/v1/user/

#### GET
##### Description:

基本用户表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| last_login | query |  | No | string |
| is_superuser | query |  | No | string |
| groups | query |  | No | string |
| user_permissions | query |  | No | string |
| first_name | query |  | No | string |
| last_name | query |  | No | string |
| email | query |  | No | string |
| is_staff | query |  | No | string |
| is_active | query |  | No | string |
| date_joined | query |  | No | string |
| username | query |  | No | string |
| password | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

### /base/v1/user/{id}/

#### GET
##### Description:

基本用户表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this User. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [User](#user) |

#### PUT
##### Description:

基本用户表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this User. | Yes | integer |
| data | body |  | Yes | [User](#user) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [User](#user) |

#### PATCH
##### Description:

基本用户表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this User. | Yes | integer |
| data | body |  | Yes | [User](#user) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [User](#user) |

### /goods/v1/category/

#### GET
##### Description:

获取商品大类列表  
    商品类别用于确认商品除基本属性外的各个属性

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | No | string |
| spec | query |  | No | string |
| father | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

新增大类  
    spec选择属性，father指定父类

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Category](#category) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Category](#category) |

### /goods/v1/category/{id}/

#### GET
##### Description:

获取单个大类信息  
    商品类别用于确认商品除基本属性外的各个属性

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this ProductCategory. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Category](#category) |

#### PUT
##### Description:

更新大类  
    全部数据

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this ProductCategory. | Yes | integer |
| data | body |  | Yes | [Category](#category) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Category](#category) |

#### PATCH
##### Description:

部分更新

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this ProductCategory. | Yes | integer |
| data | body |  | Yes | [Category](#category) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Category](#category) |

#### DELETE
##### Description:

删除资源

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this ProductCategory. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /goods/v1/product/

#### GET
##### Description:

获取商品列表 
    商品有商品历史记录

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

新增商品
    商品新增时需要不同类别定义的属性

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Product](#product) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Product](#product) |

### /goods/v1/product/{id}/

#### GET
##### Description:

获取单个大类信息  
    商品属性包含基本属性和自定义属性

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Product. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Product](#product) |

#### PUT
##### Description:

更新大类  
    更新商品

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Product. | Yes | integer |
| data | body |  | Yes | [Product](#product) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Product](#product) |

#### PATCH
##### Description:

部分更新

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Product. | Yes | integer |
| data | body |  | Yes | [Product](#product) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Product](#product) |

#### DELETE
##### Description:

删除资源

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Product. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /goods/v1/product_spec/

#### GET
##### Description:

获取商品-属性关系列表 
    所有属性

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| product | query |  | No | string |
| spec | query |  | No | string |
| speninfo | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

### /goods/v1/product_spec/{id}/

#### GET
##### Description:

获取单个信息

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this ProductSpec. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ProductSpec](#productspec) |

### /goods/v1/spec/

#### GET
##### Description:

获取商品属性列表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

#### POST
##### Description:

新增商品属性
    新增时直接同步新增SpecInfo（属性值）

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Spec](#spec) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Spec](#spec) |

### /goods/v1/spec/{id}/

#### GET
##### Description:

获取单个属性大类信息

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Spec. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Spec](#spec) |

#### PUT
##### Description:

更新大类  
    同步新增|删除SpecInfo

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Spec. | Yes | integer |
| data | body |  | Yes | [Spec](#spec) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Spec](#spec) |

#### PATCH
##### Description:

部分更新

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Spec. | Yes | integer |
| data | body |  | Yes | [Spec](#spec) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Spec](#spec) |

#### DELETE
##### Description:

删除资源

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this Spec. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

### /goods/v1/spec_info/

#### GET
##### Description:

获取属性值列表

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| spec | query |  | No | string |
| name | query |  | No | string |
| page | query | A page number within the paginated result set. | No | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | object |

### Models


#### TokenRefresh

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| refresh | string |  | Yes |

#### TokenObtainPair

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| username | string |  | Yes |
| password | string |  | Yes |

#### Group

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| permissions | [ integer ] | 数组，权限id | Yes |
| name | string | 组名 | Yes |

#### Permission

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| codename | string |  | Yes |
| content_type | object |  | No |

#### User

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| last_login | dateTime |  | No |
| is_superuser | boolean | 指明该用户缺省拥有所有权限。 | No |
| first_name | string |  | No |
| last_name | string |  | No |
| email | string (email) |  | No |
| is_staff | boolean | 指明用户是否可以登录到这个管理站点。 | No |
| is_active | boolean | 指明用户是否被认为是活跃的。以反选代替删除帐号。 | No |
| date_joined | dateTime |  | No |
| username | string | 150 characters or fewer. Letters, digits and @/./+/-/_ only. | No |
| password | string |  | No |
| groups | [ object ] |  | No |
| user_permissions | [ object ] |  | No |

#### Category

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| father | integer | int,父类 | Yes |
| name | string | string(150),类别名称,unique | Yes |
| spec | [ object ] |  | No |

#### Product

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| code | string (uuid) | string(150),商品唯一编码 | No |
| name | string | string(150),商品名称 | Yes |
| main_image | string (uri) | file,主图 | No |
| image1 | string (uri) | file,图1 | No |
| image2 | string (uri) | file,图2 | No |
| image3 | string (uri) | file,图3 | No |
| image4 | string (uri) | file,图4 | No |
| image5 | string (uri) | file,图5 | No |
| description | string | text,详情描述 | No |
| stock | integer | int,商品库存 | No |
| discount | number | float,折扣 | No |
| on_sale | boolean | bool,是否在售 | No |
| create_time | dateTime | datetime,创建时间 | No |
| update_time | dateTime | datetime,更新时间 | No |
| is_history | boolean | bool,是否历史 | No |
| category | object |  | No |

#### ProductSpec

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| product | object |  | No |
| spec | object |  | No |
| speninfo | object |  | No |

#### SpecInfo

[spec_info]数组

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string | string(50),属性值名称 | Yes |

#### Spec

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| spec_info | [ [SpecInfo](#specinfo) ] | [spec_info]数组 | Yes |
| name | string | string(50),属性名 | Yes |