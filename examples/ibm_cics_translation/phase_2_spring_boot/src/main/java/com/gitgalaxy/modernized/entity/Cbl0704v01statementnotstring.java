package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0704V01STATEMENTNOTSTRING")
public class Cbl0704v01statementnotstring {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_STR")
    private String wsStr;

    @Column(name = "WS_STR_OUT1")
    private String wsStrOut1;

    @Column(name = "WS_STR_OUT2")
    private String wsStrOut2;

    @Column(name = "WS_STR_OUT3")
    private String wsStrOut3;

    @Column(name = "WS_COUNT")
    private Integer wsCount;

}