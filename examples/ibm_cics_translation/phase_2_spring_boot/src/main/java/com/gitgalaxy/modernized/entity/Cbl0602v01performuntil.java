package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0602V01PERFORMUNTIL")
public class Cbl0602v01performuntil {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_NUM1")
    private Integer wsNum1;

    @Column(name = "WS_TOT")
    private Integer wsTot;

}