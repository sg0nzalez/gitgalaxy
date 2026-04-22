package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0106V01CLAUSULAIMAGEN")
public class Cbl0106v01clausulaimagen {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NUM1")
    private BigDecimal wsNum1;

    @Column(name = "WS_NUM2")
    private BigDecimal wsNum2;

    @Column(name = "WS_NUM3")
    private BigDecimal wsNum3;

    @Column(name = "WS_NAME")
    private String wsName;

    @Column(name = "WS_ID")
    private String wsId;

}