package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0505V01CONDICIONNAME")
public class Cbl0505v01condicionname {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_NUM")
    private BigDecimal wsNum;

}