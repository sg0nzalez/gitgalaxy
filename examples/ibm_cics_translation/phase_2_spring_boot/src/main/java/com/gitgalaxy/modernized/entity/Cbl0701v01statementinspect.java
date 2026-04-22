package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0701V01STATEMENTINSPECT")
public class Cbl0701v01statementinspect {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_N")
    private Integer wsN;

    @Column(name = "WS_STR")
    private String wsStr;

    @Column(name = "WS_TOT")
    private Integer wsTot;

}