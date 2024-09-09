* ClickHouse建表语句：https://www.yuque.com/chenweishi/xsi59x/zf53fihknui7tk3r

* 建表语句 

  * ```sql
    CREATE TABLE 预算执行报表  
    (  
        `预算id` Nullable(String),  
        `预算编号` Nullable(String),  
        `预算期间ID` Nullable(String),  
        `预算名称` Nullable(String),  
        `预算主体ID` Nullable(String),  
        `预算表项目ID` Nullable(String),  
        `预算科目` Nullable(String),  
        `成本中心` Nullable(String),  
        `项目` Nullable(String),  
        `业务线` Nullable(String),  
        `预算金额` Nullable(Float64),  
        `预算余额` Nullable(Float64),  
        `允差` Nullable(Float64),  
        `控制策略` Nullable(String),  
        `预算结转` Nullable(String),  
        `结转期间` Nullable(String),  
        `关联年度预算ID` Nullable(String),  
        `预算生效日期` Nullable(Date),  
        `预算失效日期` Nullable(Date),  
        `项目阶段` Nullable(String),  
        `产品` Nullable(String),  
        `预算主体名称` Nullable(String),  
        `预算期间` Nullable(String),  
        `预算扣减金额` Nullable(Float64),  
        `科目类别` Nullable(String),  
        `预算冻结金额` Nullable(Float64),  
        `创建日期` Nullable(DateTime),  
        `来源` Nullable(String),  
        `预算操作类型` Nullable(String),  
        `单据编号` Nullable(String),  
        `单据类型编号` Nullable(String),  
        `单据类型名称` Nullable(String),  
        `发起人` Nullable(String),  
        `币种` Nullable(String),  
        `汇率` Nullable(Float64),  
        `原币金额` Nullable(Float64),  
        `本币金额` Nullable(Float64),  
        `摘要` Nullable(String),  
        `预算执行时间` Nullable(DateTime),  
        `单据发起日期` Nullable(DateTime),  
        `总账日期` Nullable(DateTime),  
        `单据发起部门` Nullable(String),  
        `会议名称` Nullable(String),  
        `单据状态` Nullable(String),  
        `单据id` Nullable(String),  
        `备注` Nullable(String),  
        `成本中心名称` Nullable(String),  
        `预算科目名称` Nullable(String),  
        `项目阶段名称` Nullable(String),  
        `产品名称` Nullable(String),  
        `科目类别名称` Nullable(String),  
        `项目名称` Nullable(String),  
        `ad账号` Nullable(String),  
        `员工号` Nullable(String),  
        `名称` Nullable(String),  
        `预算维护表ID` Nullable(String),  
        `部门名称` Nullable(String),  
        `业务小类名称` Nullable(String),  
        `BU` Nullable(String),  
        `申请人` Nullable(String),  
        `申请人部门` Nullable(String)  
    )  
    ENGINE = MergeTree()  
    ORDER BY (`预算id`);
    ```

* 