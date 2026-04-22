package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "WS_INTERES1")
public class WsInteres1 {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_TEN")
    private BigDecimal wsTen;

    @Column(name = "WS_TEA")
    private BigDecimal wsTea;

    @Column(name = "WS_INTERES")
    private BigDecimal wsInteres;

}