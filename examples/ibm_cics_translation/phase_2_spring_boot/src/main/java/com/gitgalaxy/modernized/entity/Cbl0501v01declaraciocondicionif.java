package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0501V01DECLARACIOCONDICIONIF")
public class Cbl0501v01declaraciocondicionif {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_NUM1")
    private Integer wsNum1;

    @Column(name = "WS_NUM2")
    private Integer wsNum2;

    @Column(name = "WS_NUM3")
    private Integer wsNum3;

}