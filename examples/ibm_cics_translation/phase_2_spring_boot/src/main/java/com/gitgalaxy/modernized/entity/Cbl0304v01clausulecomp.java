package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0304V01CLAUSULECOMP")
public class Cbl0304v01clausulecomp {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_TEN")
    private BigDecimal wsTen;

    @Column(name = "WS_TEN1")
    private BigDecimal wsTen1;

    @Column(name = "WS_TEA")
    private BigDecimal wsTea;

    @Column(name = "WS_TEA1")
    private BigDecimal wsTea1;

    @Column(name = "WS_INTERES")
    private BigDecimal wsInteres;

    @Column(name = "WS_INTERES1")
    private BigDecimal wsInteres1;

}