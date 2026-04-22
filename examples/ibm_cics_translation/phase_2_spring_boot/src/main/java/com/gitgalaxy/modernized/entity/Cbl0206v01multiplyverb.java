package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0206V01MULTIPLYVERB")
public class Cbl0206v01multiplyverb {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NUM1")
    private Integer wsNum1;

    @Column(name = "WS_NUM2")
    private Integer wsNum2;

    @Column(name = "WS_NUM3")
    private Integer wsNum3;

    @Column(name = "WS_NUM4")
    private Integer wsNum4;

    @Column(name = "WS_NUMA")
    private Integer wsNuma;

    @Column(name = "WS_NUMB")
    private Integer wsNumb;

    @Column(name = "WS_NUMC")
    private Integer wsNumc;

    @Column(name = "WS_NUMD")
    private Integer wsNumd;

    @Column(name = "WS_NUMT")
    private Integer wsNumt;

}