graph TD
    subgraph "用户交互"
         A[用户输入]
     end
     
    subgraph "智能代理 (Agent)"
        B{1. Agent接收输入和状态}
        C{2. 决策: 直接回答还是使用工具?}
        D[3. 工具节点]
        E[4. Agent接收工具结果, 再次决策]
         end
     
    subgraph "可用工具集"
        T1[search_books]
        T2[recommend_by_genre]
        T3[recommend_by_author]
        T4[get_book_details]
        T5[...]
    end
     
    subgraph "输出"
        F[最终答复]
    end
     
    A --> B;
    B --> C;
    C -- 需要工具 --> D;
    D -- 调用 --> T1;
    D -- 调用 --> T2;
    D -- 调用 --> T3;
    D -- 调用 --> T4;
    D -- 调用 --> T5;
    T1 --> E;
    T2 --> E;
    T3 --> E;
    T4 --> E;
    T5 --> E;
    E --> C;
    C -- 无需工具/完成 --> F;